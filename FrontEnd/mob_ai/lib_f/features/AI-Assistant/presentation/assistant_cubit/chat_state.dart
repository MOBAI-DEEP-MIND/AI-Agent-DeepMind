part of 'chat_cubit.dart';

@immutable
abstract class ChatState {}

class ChatInitial extends ChatState {}

class ChatMessageSuccuss extends ChatState {
  final List<Message> messagesList;
  ChatMessageSuccuss(this.messagesList);
}

// ignore: must_be_immutable
class ChatMessageFailure extends ChatState {
  String errMessage;
  ChatMessageFailure(this.errMessage);
}
