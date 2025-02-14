// // import 'package:blog_app_revision/core/common/widgets/loader.dart';
// // import 'package:blog_app_revision/core/utils/snack_bar.dart';
// // import 'package:blog_app_revision/core/theme/app_pallete.dart';
// // import 'package:blog_app_revision/features/auth/presentation/bloc/auth_bloc.dart';
// // import 'package:blog_app_revision/features/auth/presentation/views/sign_in_view.dart';
// // import 'package:blog_app_revision/features/auth/presentation/widgets/auth_gradient_button.dart';
// // import 'package:blog_app_revision/features/auth/presentation/widgets/auth_field.dart';
// // import 'package:blog_app_revision/features/blogs/presentation/views/bolgs_view.dart';
// import 'package:flutter/material.dart';
// import 'package:flutter_bloc/flutter_bloc.dart';

// import '../../../../core/common/widgets/loader.dart';
// import '../../../../core/utils/snack_bar.dart';
// import '../../../home/presentation/views/home_view.dart';
// import '../bloc/auth_bloc.dart';
// import '../widgets/auth_field.dart';
// import '../widgets/auth_gradient_button.dart';
// import 'sign_in_view.dart';

// class SignUpView extends StatefulWidget {
//   const SignUpView({super.key});

//   @override
//   State<SignUpView> createState() => _SignUpViewState();
// }

// class _SignUpViewState extends State<SignUpView> {
//   final _formKey = GlobalKey<FormState>();
//   final TextEditingController _nameController = TextEditingController();
//   final TextEditingController _emailController = TextEditingController();
//   final TextEditingController _passwordController = TextEditingController();
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(),
//       body: Padding(
//         padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
//         child: SingleChildScrollView(
//           child: BlocConsumer<AuthBloc, AuthState>(
//             listener: (context, state) {
//               if (state is AuthFailure) {
//                 showSnackBar(context, state.message);
//               }
//               if (state is AuthSuccess) {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(
//                     builder: (context) {
//                       return HomeView();
//                     },
//                   ),
//                 );
//               }
//             },
//             builder: (context, state) {
//               if (state is AuthLoading) {
//                 return Loader();
//               }
//               return Column(
//                 spacing: 20,
//                 mainAxisAlignment: MainAxisAlignment.center,
//                 children: [
//                   const Text(
//                     'Sign Up.',
//                     style: TextStyle(fontSize: 52, fontWeight: FontWeight.bold),
//                   ),
//                   Form(
//                     key: _formKey,
//                     child: Column(
//                       spacing: 20,
//                       mainAxisAlignment: MainAxisAlignment.center,
//                       children: [
//                         Authfield(
//                           controller: _nameController,
//                           hintText: 'Name',
//                         ),
//                         Authfield(
//                           controller: _emailController,
//                           hintText: 'Email',
//                         ),
//                         Authfield(
//                           controller: _passwordController,
//                           hintText: 'Password',
//                           obscureText: true,
//                         ),
//                       ],
//                     ),
//                   ),
//                   AuthGradientButton(
//                     text: 'Sign Up',
//                     onTap: () {
//                       if (_formKey.currentState!.validate()) {
//                         context.read<AuthBloc>().add(
//                           AuthSignUp(
//                             name: _nameController.text.trim(),
//                             email: _emailController.text.trim(),
//                             password: _passwordController.text.trim(),
//                           ),
//                         );
//                       }

//                       _formKey.currentState!.reset();
//                     },
//                   ),
//                   GestureDetector(
//                     onTap: () {
//                       Navigator.push(
//                         context,
//                         MaterialPageRoute(
//                           builder: (context) {
//                             return SignInView();
//                           },
//                         ),
//                       );
//                     },
//                     child: RichText(
//                       text: TextSpan(
//                         text: 'Already have An Account? ',
//                         style: Theme.of(context).textTheme.titleMedium,
//                         children: [TextSpan(text: 'Sign In')],
//                       ),
//                     ),
//                   ),
//                 ],
//               );
//             },
//           ),
//         ),
//       ),
//     );
//   }

//   @override
//   void dispose() {
//     _emailController.dispose();
//     _passwordController.dispose();
//     super.dispose();
//   }
// }
