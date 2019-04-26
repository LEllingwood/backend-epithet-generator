# # tests need to start with 'test'

# def thing(num):
#     return num*2

# # run pytest on the command line : 'pytest'
    
#     # test is marked as passing if it doesn't automatically error out.  can fix this by using the 'assert' statement.

# # happy path 
# def test_thing_success():
#     # pass
#     assert thing(2) == 4
#     assert thing(3) == 6


# # sad path
# def test_thing_failure():
#     with pytest.raise(AssertionError):
#         # the line above catches the error
#         assert thing(2) == 6
# you want the function above to fail.  failure = success.

# acceptance testing

# pipenv install flask-pytest.  this is a plug in that adds in a specific client so we can work with it.

# fixture - a single function that we point pytest towards that runs every single time.  in that fixture, you set whether it should run before or after the test.

# pp - pretty print 
# test_client is added when you install flask-pytest.  it's on the app object.

# def test_app_index():
#     breakpoint()
#     result = app.test_client().get('/')
#     assert result.status_code == 200
#     assert result.data.decode() == 'heyyy'

    # .decode() - 
    # most of the web runs on unicode.  flask uses bytecode.  when you ask for the raw data included in the response, the response might be in bytes, not unicode.  so you have to run decode() to change it to unicode. result.data will give you byte code.  you could also handle it like this: assert result.data == b'heyyy'


# coverage = generally make sure that the code is testing.  the number of tests doesn't really matter.  aim for 80% coverage.  