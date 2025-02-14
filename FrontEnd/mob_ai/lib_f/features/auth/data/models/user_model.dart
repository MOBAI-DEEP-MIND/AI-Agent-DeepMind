
import '../../../../core/common/entities/user.dart';

class UserModel extends User {
  UserModel({
    required super.id,
    required super.username,
    required super.email,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id']  ?? 0,
     username: json['name'] ?? '',
      email: json['email'] ?? '',
    );
  }
  UserModel copyWith({int? id, String? username, String? email}) {
    return UserModel(
      id: id ?? this.id,
      username: username ?? this.username,
      email: email ?? this.email,
    );
  }

}
