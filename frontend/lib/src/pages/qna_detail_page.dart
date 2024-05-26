import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;
import '../components/post_widget.dart';

class PostDetailPage extends StatefulWidget {
  final Post post;

  const PostDetailPage({Key? key, required this.post}) : super(key: key);

  @override
  _PostDetailPageState createState() => _PostDetailPageState();
}

class _PostDetailPageState extends State<PostDetailPage> {
  List<Comment> comments = [];

  @override
  void initState() {
    super.initState();
    _loadComments();
  }

  Future<void> _loadComments() async {
    final String response =
        await rootBundle.loadString('assets/test_json/comments.json');
    final List<dynamic> data = json.decode(response);
    setState(() {
      comments = (data.firstWhere(
              (item) => item['postId'] == widget.post.id)['comments'] as List)
          .map((comment) => Comment.fromJson(comment))
          .toList();
    });
  }

  void _addComment(String content) {
    setState(() {
      comments.add(Comment(author: "CurrentUser", content: content));
      // 여기에 새로운 댓글을 서버나 파일에 저장하는 로직을 추가할 수 있습니다.
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.post.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(widget.post.content, style: TextStyle(fontSize: 18)),
            SizedBox(height: 20),
            Text('Comments',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            Expanded(
              child: ListView(
                children: comments
                    .map((comment) => ListTile(
                          title: Text(comment.author),
                          subtitle: Text(comment.content),
                        ))
                    .toList(),
              ),
            ),
            TextField(
              decoration: InputDecoration(
                labelText: 'Add a comment',
                border: OutlineInputBorder(),
              ),
              onSubmitted: (value) {
                _addComment(value);
              },
            ),
          ],
        ),
      ),
    );
  }
}
