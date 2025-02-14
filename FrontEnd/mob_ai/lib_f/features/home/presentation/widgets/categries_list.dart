import 'package:flutter/material.dart';

import '../../../../core/constants/constants.dart';

class CategoriesList extends StatefulWidget {
  const CategoriesList({super.key, required this.selectedTopics});
  final List<String> selectedTopics;

  @override
  State<CategoriesList> createState() => _CategoriesListState();
}

class _CategoriesListState extends State<CategoriesList> {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        children:
            Constants.categories
                .map(
                  (e) => Padding(
                    padding: const EdgeInsets.only(
                      top: 5.0,
                      bottom: 5.0,
                      right: 5.0,
                    ),
                    child: GestureDetector(
                      onTap: () {
                        if (widget.selectedTopics.contains(e)) {
                          widget.selectedTopics.remove(e);
                        } else {
                          widget.selectedTopics.add(e);
                        }
                        setState(() {});
                      },
                      child: Chip(
                        padding: const EdgeInsets.all(8
                        ),
                        color:
                            widget.selectedTopics.contains(e)
                                ? WidgetStatePropertyAll(Colors.black)
                                : null,
                        label: Text(
                          e,
                          style: TextStyle(
                            color:
                                widget.selectedTopics.contains(e)
                                    ? Colors.white
                                    : null,
                          ),
                        ),
                      ),
                    ),
                  ),
                )
                .toList(),
      ),
    );
  }
}

class CategoryItem extends StatelessWidget {
  const CategoryItem({super.key});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}
