// import 'package:blog_app_revision/core/common/cubits/app_user/app_user_cubit.dart';
// import 'package:blog_app_revision/core/usecase/use_case.dart';
// import 'package:blog_app_revision/core/common/entities/user.dart';
// import 'package:blog_app_revision/features/auth/domain/usecases/current_user.dart';
// import 'package:blog_app_revision/features/auth/domain/usecases/user_sign_in.dart';
// import 'package:blog_app_revision/features/auth/domain/usecases/user_sign_up.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../../../core/common/cubits/app_user/app_user_cubit.dart';
import '../../../../core/common/entities/user.dart' show User;
import '../../domain/usecases/user_sign_in.dart';
import '../../domain/usecases/user_sign_up.dart';

part 'auth_event.dart';
part 'auth_state.dart';

class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final UserSignUp _userSignUp;
  final UserSignIn _userSignIn;
  final AppUserCubit _appUserCubit;
  AuthBloc({
    required UserSignUp userSignUp,
    required UserSignIn userSignIn,
    required AppUserCubit appUserCubit,
  })  : _userSignUp = userSignUp,
        _userSignIn = userSignIn,
        _appUserCubit = appUserCubit,
        super(AuthInitial()) {
    on<AuthEvent>(
      (_, emit) => emit(
        AuthLoading(),
      ),
    );
    on<AuthSignUp>(
      _onAuthSignUp,
    );
    on<AuthSignIn>(
      _onAuthSignIn,
    );
    // on<AuthIsUserLoggedIn>(
    //   _isUserLoggedIn,
    // );
  }
  // void _isUserLoggedIn(event, emit) async {
  //   final res = await _currentUser(NoParams());
  //   res.fold((failure) {
  //     emit(
  //       AuthFailure(
  //         failure.errMessage,
  //       ),
  //     );
  //   }, (user) {
  //     _emitAuthStateSuccess(user, emit);
  //   });
  // }

  void _onAuthSignUp(event, emit) async {
    final res = await _userSignUp(UserSignUpParams(
        name: event.username, email: event.email, password: event.password));
    res.fold((failure) {
      emit(
        AuthFailure(
          failure.errMessage,
        ),
      );
    }, (user) {
      _emitAuthStateSuccess(user, emit);
    });
  }

  void _onAuthSignIn(event, emit) async {
    final res = await _userSignIn(
        UserSignInParams(email: event.email, password: event.password));
    res.fold((failure) {
      emit(
        AuthFailure(
          failure.errMessage,
        ),
      );
    }, (user) {
      _emitAuthStateSuccess(user, emit);
    });
  }

  void _emitAuthStateSuccess(User user, Emitter<AuthState> emit) {
    _appUserCubit.updateUser(user);
    emit(AuthSuccess(user));
  }
}
