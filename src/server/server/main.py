from flask import Flask
from markupsafe import escape

from common import Serializer, JSONSerializer
from server.extraction import HTMLExtractor, Extractor


def split_url_word(url_word: str) -> str:
    return ' '.join(url_word.split('+'))


app = Flask(__name__)

extractor: Extractor = HTMLExtractor()
serializer: Serializer = JSONSerializer()


@app.route('/timetable/<group_id>')
def get_timetable(group_id: str):
    return serializer.serialize(extractor.extract_timetable(escape(group_id)))


@app.route('/room/<room_name>')
def get_room(room_name: str):
    return serializer.serialize(extractor.extract_room(split_url_word(escape(room_name))))


@app.route('/tutor/<tutor_name>')
def get_tutor(tutor_name: str):
    return serializer.serialize(extractor.extract_tutor(split_url_word(escape(tutor_name))))


@app.route('/times')
def get_times():
    return serializer.serialize(extractor.extract_times())


app.run()
