from app.doc import parameter, JWT_ACCESS_TOKEN

SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',
    'parameters': [
        parameter('name', '이름'),
        parameter('id', '사용자 아이디'),
        parameter('password', '사용자 비밀번호')
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '205': {
            'description': '가입 불가능(중복된 ID)'
        }
    }
}

ADDITIONAL_PATCH = {
    'tags': ['Account'],
    'description': '추가 세부 내용',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('gender', '이름'),
        parameter('age', '나이'),
        parameter('address', '주소'),
        parameter('intro', '한 줄 소개'),
    ],
    'responses': {
        '201': {
            'description': '추가 완료'
        },
        '205': {
            'description': '없는 ID'
        }
    }
}