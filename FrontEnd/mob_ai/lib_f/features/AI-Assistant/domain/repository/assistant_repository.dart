import 'package:fpdart/fpdart.dart';

import '../../../../core/error/failure.dart';
import '../entity/message.dart';

abstract interface class AssistantRepository {
  Future <Either<Failure, Message>> sendMessage({required Message message});
}