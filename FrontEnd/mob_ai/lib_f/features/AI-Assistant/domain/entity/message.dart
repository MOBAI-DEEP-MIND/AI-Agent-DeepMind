// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';

class Message {
  final String senderId;
  final String? messageId;
  final String content;

  Message({
    required this.senderId,
    this.messageId,
    required this.content,
  });

  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'senderId': senderId,
      'messageId': messageId,
      'content': content,
    };
  }

  factory Message.fromMap(Map<String, dynamic> map) {
    return Message(
      senderId: map['senderId'] as String,
      messageId: map['messageId'] != null ? map['messageId'] as String : null,
      content: map['content'] as String,
    );
  }

  String toJson() => json.encode(toMap());

  factory Message.fromJson(String source) => Message.fromMap(json.decode(source) as Map<String, dynamic>);

  Message copyWith({
    String? senderId,
    String? messageId,
    String? content,
  }) {
    return Message(
      senderId: senderId ?? this.senderId,
      messageId: messageId ?? this.messageId,
      content: content ?? this.content,
    );
  }
}
