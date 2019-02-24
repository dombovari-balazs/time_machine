from flask import Flask, render_template
import connection
import arabic_to_roman

app = Flask(__name__)


@app.route('/')
def numbers():
    arabic_numbers = connection.get_numbers_from_file('ARAB.IN')
    roman_numbers = [arabic_to_roman.get_result_under_4000(int(number)) for number in arabic_numbers]
    connection.write_table_to_file('ROMAI.OUT', roman_numbers, arabic_numbers)
    return render_template('main.html', roman_numbers=roman_numbers, arabic_numbers=arabic_numbers)


if __name__ == '__main__':
    app.run()
