# Test
* [main](docs/main.md)
* [menu methods](docs/menu.md)
## GET
```
GET /{text4}
```
### success
#### example
```json
head status: 200
{
    "a": 1212321,
    "b": {
        "sadas": true
    }
}
```
### errors
#### fields
##### text4 
```json

head status: 400
{
    "help": "Field is not Integer",
    "message": "('Field \"%s\" is not Integer, %s' % (self.name, e))"
}
```
##### text 
```json

head status: 400
{
    "help": "Value is not Less",
    "message": "('Field \"%s\" %s <%s %s' % (self.name, self.value, eq, self.less))"
}
head status: 400
{
    "help": "Value is not Larger",
    "message": "('Field \"%s\" %s >%s %s' % (self.name, self.value, eq, self.larger))"
}
head status: 400
{
    "help": "Field is not Integer",
    "message": "('Field \"%s\" is not Integer, %s' % (self.name, e))"
}
```
#### method
```json

head status: 401
{
    "message": "asfasfasf"
}
```
## POST
```
POST /{text4}
```
### success
#### example
```json
head status: 201
null
```
### errors
#### fields
##### text4 
```json

head status: 400
{
    "help": "Field is not Integer",
    "message": "('Field \"%s\" is not Integer, %s' % (self.name, e))"
}
```
##### text 
```json

head status: 400
{
    "help": "Value is not Less",
    "message": "('Field \"%s\" %s <%s %s' % (self.name, self.value, eq, self.less))"
}
head status: 400
{
    "help": "Value is not Larger",
    "message": "('Field \"%s\" %s >%s %s' % (self.name, self.value, eq, self.larger))"
}
head status: 400
{
    "help": "Field is not Integer",
    "message": "('Field \"%s\" is not Integer, %s' % (self.name, e))"
}
```