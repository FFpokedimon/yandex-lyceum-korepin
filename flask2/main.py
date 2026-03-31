from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def main_index_title(title):
    return render_template("base.html", title=title)


@app.route('/promotion')
def promotion():
    return '''
<p>
    Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!
</p>
    '''


@app.route('/image_mars')
def image_mars():
    return f'''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}">
    <p>Вот она какая, красная планета.</p>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</body>
</html>
    '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="{url_for('static', filename='css/promotion_image.css')}" rel="stylesheet">
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}">
    <p class="alert alert-light">Человечество вырастает из детства.</p>
    <p class="alert alert-success">Человечеству мала одна планета.</p>
    <p class="alert alert-light">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="alert alert-warning">И начнем с Марса!</p>
    <p class="alert alert-danger">Присоединяйся!</p>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</body>
</html>
    '''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/astronaut_selection.css')}"/>
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 class="fw-bold">Анкета претендента</h1>
<h2>на участие в миссии</h2>
<div>
    <form class="request_form" method="post">
        <div class="form-group">
            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
            <input type="text" class="form-control" id="forename" placeholder="Введите имя" name="forename">
        </div>
        <br>
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
               placeholder="Введите адрес почты" name="email">
        <br>
        <div class="form-group">
            <div class="form-group">
                <label for="educationSelect">Какое у Вас образование?</label>
                <select class="form-control" id="educationSelect" name="education">
                    <option value="primary">Начальное</option>
                    <option value="secondary">Среднее</option>
                    <option value="higher">Высшее</option>
                </select>
            </div>
            <label for="professionCheck">Какие у Вас есть профессии?</label>
            <div class="form-check" id="professionCheck">
                <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                <label class="form-check-label" for="pilot">Пилот</label>
                <br>
                <input type="checkbox" class="form-check-input" id="meteorologist" name="meteorologist">
                <label class="form-check-label" for="meteorologist">Метеоролог</label>
                <br>
                <input type="checkbox" class="form-check-input" id="exobiologist" name="exobiologist">
                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
            </div>
        </div>
        <br>
        <div class="form-group">
            <label for="about">Почему Вы хотите принять участие в миссии?</label>
            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
        </div>
        <br>
        <div class="form-group">
            <label for="genderRadio">Укажите пол</label>
            <div class="form-check" id="genderRadio">
                <input class="form-check-input" type="radio" name="gender" id="male" value="male" checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="gender" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
        </div>
        <br>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <br>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</div>
</body>
</html>
        '''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet>')
def planet_choice(planet):
    return f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Варианты выбора</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
    <h1>Мое предложение: {planet}</h1>
    <p>Эта планета близка к земле;</p>
    <div class="alert alert-success">На ней есть много необходимых ресурсов;</div>
    <div class="alert alert-secondary">На ней есть вода и атмосфера;</div>
    <div class="alert alert-warning">На ней есть небольшое магнитное поле;</div>
    <div class="alert alert-danger">Наконец, она просто красива!</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</body>
</html>
    '''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}</h2>
    <div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
    <p>составляет {rating}</p>
    <div class="alert alert-warning">Желаем удачи!</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</body>
</html>
    '''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/load_photo.css')}"/>
    <title>Отбор астронавтов</title>
</head>
<body>
    <h1 class="fw-bold">Загрузка фотографии</h1>
    <h2>для участия в миссии</h2>
    <div>
        <form class="request_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <img src="{url_for('static', filename='img/photo.jpg')}">
            <br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
                crossorigin="anonymous"></script>
    </div>
</body>
</html>
        '''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/photo.jpg', 'wb') as file:
            file.write(f.stream.read())
        return redirect(url_for('load_photo'))


@app.route('/carousel')
def carousel():
    return f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пейзажи Марса</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
    <h1 class="text-center my-3">Пейзажи Марса</h1>
    <div id="carouselExampleIndicators" class="carousel slide w-50 mx-auto" data-bs-ride="carousel">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="{url_for('static', filename='img/landscapes/landscape1.jpg')}" class="d-block w-100">
            </div>
            <div class="carousel-item">
                <img src="{url_for('static', filename='img/landscapes/landscape2.jpg')}" class="d-block w-100">
            </div>
            <div class="carousel-item">
                <img src="{url_for('static', filename='img/landscapes/landscape3.jpg')}" class="d-block w-100">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
            crossorigin="anonymous"></script>
</body>
</html>
'''


@app.route('/training/<string:prof>')
def training(prof):
    return render_template("training.html", prof=prof)


@app.route('/list_prof/<string:list_type>')
def list_prof(list_type):
    return render_template("list_prof.html", list_type=list_type)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
