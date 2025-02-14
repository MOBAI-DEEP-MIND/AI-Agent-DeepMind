import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../domain/entity/message.dart';
import '../../domain/usecase/send_message.dart';

part 'chat_state.dart';

class ChatCubit extends Cubit<ChatState> {
  final SendMessage _sendMessage;
  ChatCubit({required SendMessage sendMessage})
    : _sendMessage = sendMessage,
      super(ChatInitial());

  List<Message> messagesList = [];
  void sendMessage({required Message message}) async {
    try {
      final response = await _sendMessage(MessageParams(message: message));
      response.fold(
        (failure) {
          emit(ChatMessageFailure(failure.errMessage));
        },
        (success) {
          log('${success.content} ${success.senderId}');
          messagesList.add(success);
        },
      );
    } catch (e) {
      emit(ChatMessageFailure(e.toString()));
    }
  }
}
