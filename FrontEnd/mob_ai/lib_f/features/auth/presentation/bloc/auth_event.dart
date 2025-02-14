part of 'auth_bloc.dart';

@immutable
sealed class AuthEvent {}

class AuthSignUp extends AuthEvent {
  final String email;
  final String password;
  final String name;
  AuthSignUp({
    key,
    required this.email,
    required this.password,
    required this.name,
  });
}
class AuthSignIn extends AuthEvent {
  final String email;
  final String password;
  AuthSignIn({
    key,
    required this.email,
    required this.password,
  });
}
class AuthIsUserLoggedIn extends AuthEvent {}
