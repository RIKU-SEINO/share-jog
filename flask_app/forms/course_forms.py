from flask_app.forms import *

class CreateCourseForm(FlaskForm):
    route_latlng = StringField(
        "経路の緯度経度情報",
        validators=[
            DataRequired("経路の緯度経度情報は必須です。"),
        ],
    )
    waypoint_indices = StringField(
        "経路の主要経由地点情報",
        validators=[
            DataRequired("経路の主要経由地点情報は必須です。")
        ]
    )
    title = StringField(
        "コースのタイトル",
        validators=[
            DataRequired("コースタイトルは必須です。"),
            Length(1, 50, "50文字以内で入力してください。")
        ],
    )
    description = TextAreaField(
        "コースの説明",
        validators=[
            Length(0, 200, "200文字以内で入力してください。")
        ]
    )
    distance = FloatField(
        "距離(km)",
        validators=[
            DataRequired("距離は必須です。"),
            NumberRange(min=0, message="距離は0以上の数を入力してください。")
        ],
    )
    prefecture = QuerySelectField(
        "都道府県",
        query_factory=prefecture_query,
        get_label='name',
        validators=[DataRequired("都道府県は必須です。")]
    )
    city = SelectField(
        "市区町村",
        choices=[],
        validate_choice=False
    )
    facilities = QuerySelectMultipleField(
        "近くの施設",
        query_factory=facility_query,
        get_label='name',
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )
    submit = SubmitField("保存")

class EditCourseForm(CreateCourseForm):
    is_public = BooleanField('このコースを公開して保存', default=False)
    course_images = FileField(
        "コースの画像",
        validators=[
            Length(max=255, message='ファイル名は255文字以下で入力してください。'),
            FileAllowed(['jpg', 'jpeg', 'png'], "jpgn jpeg, pngのみサポートしております。"),
        ],render_kw={"multiple": True}
    )

class SearchCourseForm(CreateCourseForm):
    freeword = StringField(
        "フリーワード"
    )
    prefecture = QuerySelectField(
        "都道府県",
        query_factory=prefecture_query,
        get_label='name',
    )
    distance_min = SelectField(
        "最小距離",
        choices=[
            ('', '指定なし'),
            (1, '1km'),
            (2, '2km'),
            (3, '3km'),
            (5, '5km'),
            (10, '10km'),
            (15, '15km'),
            (20, '20km'),
            (30, '30km'),
            (50, '50km'),
        ]
    )
    distance_max = SelectField(
        "最大距離",
        choices=[
            ('', '指定なし'),
            (1, '1km'),
            (2, '2km'),
            (3, '3km'),
            (5, '5km'),
            (10, '10km'),
            (15, '15km'),
            (20, '20km'),
            (30, '30km'),
            (50, '50km'),
        ]
    )
    submit = SubmitField("検索")
