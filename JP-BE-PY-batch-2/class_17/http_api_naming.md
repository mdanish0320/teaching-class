@app.route("/post")
def get_all_posts():
    return "all posts"
  
@app.route("/post/1000")
def get_single_post():
    return "single post"
  
@app.route("/post/1000/comments")
def get_all_comments_of_post():
    return "all comments of a post"
  
@app.route("/post/1000/comments/50")
def get_comment_of_a_post():
    return "a single comment of the pose"  
  

@app.route("/users")
def get_all_users():
    return "all users"

@app.route("/users/200")
def get_single_user():
    return "a single user"

@app.route("/users/100/post")
def get_all_posts_of_user():
    return "all posts of the one user"

@app.route("/users/100/posts/6")
def get_single_post_of_user():
    return "a single post of one user"




