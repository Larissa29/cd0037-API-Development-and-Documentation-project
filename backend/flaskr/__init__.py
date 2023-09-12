from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions=[]

    if selection:
        questions = [question.format() for question in selection]
    return questions[start:end]


def create_app(db_URI='', test_config=None):
    # create and configure the app
    app = Flask(__name__)
    if db_URI:
        setup_db(app, db_URI)
    else:
        setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response


    @app.route("/categories", methods=['GET'])
    def get_all_categories():
        categories = Category.query.all()
        if not categories:
            abort(400)
        return jsonify({
            "success": True,
            "categories": [category.format() for category in categories],
        })


    @app.route('/questions', methods=['GET'])
    def get_questions():
        questions = Question.query.all()
        all_categories = Category.query.all()

        paginated_questions = paginate_questions(request, questions)

        if len(paginated_questions) == 0:
            abort(404)


        return jsonify({
            'success': True,
            'questions': paginated_questions,
            'total_questions': len(questions),
            "categories": [category.format() for category in all_categories]
        })


    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id: int):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if not question:
                abort(404)

            question.delete()
            selection = Question.query.all()
            categories = Category.query.all()
            return jsonify({
                'success': True,
                'delete': question_id,
                "questions": paginate_questions(request, selection),
                "total_questions": len(selection),
                "categories": [category.format() for category in categories],
            })

        except():
            abort(422)


    @app.route('/questions/create', methods=['POST'])
    def create_question():
        body = request.get_json()


        if not ('question' in body and 'answer' in body and
                'difficulty' in body and 'category' in body):
            abort(422)

        question = body.get('question', None)
        answer = body.get('answer', None)
        category = int(body.get('category', None))
        difficulty = body.get('difficulty', None)

        if not category == 1:
            category += 1

        try:
            new_question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
            new_question.insert()

            selection = Question.query.all()

            return jsonify({
                'success': True,
                'created': new_question.id,
                'questions': paginate_questions(request, selection),
                'total_questions': len(selection)
            })
        except():
            abort(422)


    @app.route('/questions/search', methods=['POST'])
    def search_question():
        body = request.get_json()
        search_term = body.get('searchTerm')

        questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

        if not questions:
            abort(400)

        return jsonify({
            'success': True,
            'questions': paginate_questions(request, questions) if questions else [],
            'total_questions': len(questions),
        })


    @app.route('/categories/<category_id>/questions', methods=['GET'])
    def get_questions_by_category(category_id):
        questions = Question.query.filter(Question.category == category_id).all()
        current_category = Category.query.filter(Category.id==category_id).one_or_none()
        if not questions:
            abort(400)

        if questions:
            return jsonify({
                'success': True,
                'questions': paginate_questions(request, questions),
                'total_questions': len(questions),
                'current_category': current_category.format()
            })


    @app.route('/quizzes', methods=['POST'])
    def start_quizz():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions')
            quiz_category = body.get('quiz_category')

            if not quiz_category:
                abort(422)

            if quiz_category['id'] == 0:
                questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
            else:
                category_id = int(quiz_category['id']) + 1
                questions = Question.query.filter(Question.category == category_id, Question.id.notin_(previous_questions)).all()

            return jsonify({
                'success': True,
                'question': random.choice(questions).format() if questions else None
            })
        except():
            abort(422)


    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({"success": False, "error": 400, "message": "bad request"}),
                400)


    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )


    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )


    @app.errorhandler(500)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 500, "message": "internal server error"}),
            405,
        )

    return app

