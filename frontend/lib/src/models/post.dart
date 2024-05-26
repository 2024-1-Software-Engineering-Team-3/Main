class Post {
  final int id;
  final String title;
  final String content;
  final int point;

  Post({
    required this.id,
    required this.title,
    required this.content,
    required this.point,
  });

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(
      id: json['id'],
      title: json['title'],
      content: json['content'],
      point: json['point'],
    );
  }
}

class Comment {
  final String author;
  final String content;

  Comment({required this.author, required this.content});

  factory Comment.fromJson(Map<String, dynamic> json) {
    return Comment(
      author: json['author'],
      content: json['content'],
    );
  }
}
