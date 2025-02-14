import 'package:flutter/material.dart';

class CustomAppBar extends StatelessWidget {
  const CustomAppBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,

      children: [
        _buildProfileAvatar(),
        Expanded(
          child: Padding(
            padding: EdgeInsets.symmetric(horizontal: 8),
            child: Container(
              decoration: BoxDecoration(
                color: Colors.grey[100],
                borderRadius: BorderRadius.circular(4),
              ),
              alignment: Alignment.center,
              child: TextField(
                decoration: InputDecoration(
                  hintText: 'Search...',

                  prefixIcon: Icon(Icons.search, color: Colors.grey[600]),
                  border: InputBorder.none,
                ),
              ),
            ),
          ),
        ),

        _buildNavIcon(Icons.shopping_cart_rounded, 'Messaging'),
      ],
    );
  }

  Widget _buildNavIcon(IconData icon, String tooltip) {
    return Icon(icon, size: 35, color: Colors.grey[700]);
  }

  void _handleIconPress(String tooltip) {
    // Handle icon taps
    print('$tooltip tapped!');
  }

  Widget _buildProfileAvatar() {
    return GestureDetector(
      onTap: () => _showProfileMenu(),
      child: SizedBox(
        height: 40,
        width: 40,
        child: CircleAvatar(
          radius: 14,
          backgroundColor: Colors.grey[300],
          backgroundImage: NetworkImage(
            'https://randomuser.me/api/portraits/men/1.jpg',
          ), // Replace with your image
        ),
      ),
    );
  }

  void _showProfileMenu() {
    // Show profile dropdown menu
  }
}
