import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../domain/entity/message.dart';
import '../assistant_cubit/chat_cubit.dart';
import '../widgets/Custom_chat_buble.dart';

// ignore: must_be_immutable
class ChatView extends StatefulWidget {
  const ChatView({super.key});

  @override
  State<ChatView> createState() => _ChatViewState();
}

class _ChatViewState extends State<ChatView> {
  // CollectionReference messages =
  final _scrollController = ScrollController();

  String message = "";

  TextEditingController controller = TextEditingController();

   List<Message> messagesList = [];
  @override
  void initState() {
    super.initState();
    messagesList = [];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        leading: IconButton(
          onPressed: () {},
          icon: Icon(CupertinoIcons.left_chevron),
        ),
        title: const Text(
          "AI Assistant",
          style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: BlocConsumer<ChatCubit, ChatState>(
              listener: (context, state) {
                if (state is ChatMessageSuccuss) {}
              },
              builder: (context, state) {
                messagesList = BlocProvider.of<ChatCubit>(context).messagesList;
                return ListView.builder(
                  controller: _scrollController,
                  itemCount: messagesList.length,
                  itemBuilder: (context, index) {
                    return  messagesList[index].senderId != "1" ? ChatBuble(message: messagesList[index].content) : HumanChatBuble(message: messagesList[index]);
                  },
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: TextField(
              controller: controller,

              decoration: InputDecoration(
                hintText: "send Message",
                suffixIcon: IconButton(
                  onPressed: () {
                    if (controller.text.isNotEmpty) {
                      var sendedMessage = Message(
                        content: controller.text.trim(),
                        senderId: "1",
                      );
                      messagesList.add(sendedMessage);

                      controller.clear();
                      context.read<ChatCubit>().sendMessage(
                        message: sendedMessage,
                      );

                      setState(() {});
                    }
                  },
                  icon: const Icon(Icons.send, size: 30),
                ),
                border: const OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.purple),
                  borderRadius: BorderRadius.all(Radius.circular(30)),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
