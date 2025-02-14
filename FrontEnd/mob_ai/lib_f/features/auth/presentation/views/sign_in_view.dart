// // import 'package:blog_app_revision/core/common/widgets/loader.dart';
// // import 'package:blog_app_revision/core/utils/snack_bar.dart';
// // import 'package:blog_app_revision/core/theme/app_pallete.dart';
// // import 'package:blog_app_revision/features/auth/presentation/bloc/auth_bloc.dart';
// // import 'package:blog_app_revision/features/auth/presentation/views/sign_up_view.dart';
// // import 'package:blog_app_revision/features/auth/presentation/widgets/auth_gradient_button.dart';
// // import 'package:blog_app_revision/features/auth/presentation/widgets/auth_field.dart';
// // import 'package:blog_app_revision/features/blogs/presentation/views/bolgs_view.dart';
// // import 'package:flutter/material.dart';
// // import 'package:flutter_bloc/flutter_bloc.dart';

// import 'package:flutter/material.dart';
// import 'package:flutter_bloc/flutter_bloc.dart';

// import '../../../../core/common/widgets/loader.dart';
// import '../../../../core/utils/snack_bar.dart';
// import '../../../home/presentation/views/home_view.dart';
// import '../bloc/auth_bloc.dart';
// import '../widgets/auth_field.dart';
// import '../widgets/auth_gradient_button.dart';
// import 'sign_up_view.dart';

// class SignInView extends StatefulWidget {
//   const SignInView({super.key});

//   @override
//   State<SignInView> createState() => _SignInViewState();
// }

// class _SignInViewState extends State<SignInView> {
//   final _formKey = GlobalKey<FormState>();
//   final TextEditingController _emailController = TextEditingController();
//   final TextEditingController _passwordController = TextEditingController();
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Padding(
//         padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
//         child: BlocConsumer<AuthBloc, AuthState>(
//           listener: (context, state) {
//             if (state is AuthFailure) {
//               showSnackBar(context, state.message);
//             } else if (state is AuthSuccess) {
//               Navigator.push(
//                 context,
//                 MaterialPageRoute(builder: (context) {
//                   return HomeView();
//                 }),
//               );
//             }
//           },
//           builder: (context, state) {
//             if (state is AuthLoading) {
//               return const Loader();
//             }
//             return Column(
//               spacing: 20,
//               mainAxisAlignment: MainAxisAlignment.center,
//               children: [
//                 const Text(
//                   'Sign In.',
//                   style: TextStyle(fontSize: 52, fontWeight: FontWeight.bold),
//                 ),
//                 Form(
//                   key: _formKey,
//                   child: Column(
//                     spacing: 20,
//                     mainAxisAlignment: MainAxisAlignment.center,
//                     children: [
//                       Authfield(
//                         controller: _emailController,
//                         hintText: 'Email',
//                       ),
//                       Authfield(
//                         controller: _passwordController,
//                         hintText: 'Password',
//                         obscureText: true,
//                       ),
//                     ],
//                   ),
//                 ),
//                 AuthGradientButton(
//                   text: 'Sign In',
//                   onTap: () {
//                     if (_formKey.currentState!.validate()) {
//                       context.read<AuthBloc>().add(AuthSignIn(
//                             email: _emailController.text.trim(),
//                             password: _passwordController.text.trim(),
//                           ));
//                     }
//                   },
//                 ),
//                 GestureDetector(
//                   onTap: () {
//                     Navigator.push(
//                       context,
//                       MaterialPageRoute(
//                         builder: (context) {
//                           return SignUpView();
//                         },
//                       ),
//                     );
//                   },
//                   child: RichText(
//                     text: TextSpan(
//                       text: 'Don\'t have An Account? ',
//                       style: Theme.of(context).textTheme.titleMedium,
//                       children: [
//                         TextSpan(
//                           text: 'Sign Up',
//                         )
//                       ],
//                     ),
//                   ),
//                 ),
//               ],
//             );
//           },
//         ),
//       ),
//     );
//   }

//   @override
//   void dispose() {
//     super.dispose();
//   }
// }
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../core/common/widgets/loader.dart';
import '../../../../core/utils/snack_bar.dart';
import '../bloc/auth_bloc.dart';
import '../widgets/auth_text_field.dart';

class SignInView extends StatefulWidget {
  const SignInView({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _SignInViewState createState() => _SignInViewState();
}

class _SignInViewState extends State<SignInView> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();

  final _passwordController = TextEditingController();
  bool _obscurePassword = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(24),
        child: BlocConsumer<AuthBloc, AuthState>(
          listener: (context, state) {
            if (state is AuthFailure) {
              showSnackBar(context, state.message);
            } else if (state is AuthSuccess) {
              // navigate
              print('success');
            }
          },
          builder: (context, state) {
            if (state is AuthLoading) {
              return Loader();
            }
            return SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    color: Colors.yellow,
                    height: MediaQuery.of(context).size.height / 5,
                    width: double.infinity,
                  ),
                  SizedBox(height: 60),
                  Text(
                    'Welcome Back!',
                    style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'Sign in to continue your reading journey',
                    style: TextStyle(fontSize: 16, color: Colors.grey[600]),
                  ),
                  SizedBox(height: 40),
                  Form(
                    key: _formKey,
                    child: Column(
                      children: [
                        AuthTextField(
                          controller: _emailController,
                          label: 'Email',
                          icon: Icons.email_outlined,
                          validator:
                              (value) => value!.isEmpty ? 'Enter email' : null,
                        ),

                        // Password Field
                        AuthTextField(
                          controller: _passwordController,
                          label: 'Password',
                          icon: Icons.lock_outline,
                          obscureText: _obscurePassword,
                          suffixIcon: IconButton(
                            icon: Icon(
                              _obscurePassword
                                  ? Icons.visibility_off
                                  : Icons.visibility,
                            ),
                            onPressed:
                                () => setState(
                                  () => _obscurePassword = !_obscurePassword,
                                ),
                          ),
                          validator:
                              (value) =>
                                  value!.length < 6
                                      ? 'Minimum 6 characters'
                                      : null,
                        ),
                      ],
                    ),
                  ),

                  // Email Field
                  SizedBox(height: 24),
                  GestureDetector(
                    onTap: () {
                      if (_formKey.currentState!.validate()) {
                        context.read<AuthBloc>().add(
                          AuthSignIn(
                            email: _emailController.text.trim(),
                            password: _passwordController.text.trim(),
                          ),
                        );
                      }
                    },
                    child: Container(
                      padding: EdgeInsets.symmetric(
                        horizontal: 20,
                        vertical: 10,
                      ),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(10),
                        color: Colors.black,
                      ),
                      alignment: Alignment.center,
                      width: double.infinity,
                      child: Text(
                        "Sign in",
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  SizedBox(height: 24),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        "Don't have an account? ",
                        style: TextStyle(
                          fontWeight: FontWeight.w600,
                          fontSize: 15,
                        ),
                      ),
                      TextButton(
                        onPressed:
                            () => Navigator.pushNamed(context, '/signup'),
                        child: Text('Sign Up'),
                      ),
                    ],
                  ),
                ],
              ),
            );
          },
        ),
      ),
    );
  }
}
