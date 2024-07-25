from marshmallow import Schema, fields

class ItemSchema(Schema):
	# id 필드가 직렬화 과정에서만 사용되고, (서버->클라)
	# 역직렬화과정에서는 무시된다 (클라->서버)
	# 즉, id 값은 서버에서 관리하겠다는 뜻
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()