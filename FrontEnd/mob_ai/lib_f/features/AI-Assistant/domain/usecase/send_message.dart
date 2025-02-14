import 'package:fpdart/src/either.dart';

import '../../../../core/error/failure.dart';
import '../../../../core/usecase/use_case.dart';
import '../entity/message.dart';
import '../repository/assistant_repository.dart';

class SendMessage implements UseCase<Message, MessageParams> {
  final AssistantRepository assisstantRepository;
  SendMessage(this.assisstantRepository);
  @override
  Future<Either<Failure, Message>> call(params) async {
    return await assisstantRepository.sendMessage(message: params.message);
  }
}

class MessageParams {
  final Message message;
  MessageParams({required this.message});
}
