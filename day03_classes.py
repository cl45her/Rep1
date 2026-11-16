class ContextManager:
    def __init__(self,max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.messages = []
        self.current_tokens = 0
    def add_message(self, role: str, content: str, tokens: int) -> bool:
        if self.max_tokens < tokens + self.current_tokens:
            return False
        else:
            self.messages.append({'role': role, "content": content})
            self.current_tokens += tokens
            return True
    def get_remaining_tokens(self) -> int:
        return self.max_tokens - self.current_tokens
class SystemContextManager(ContextManager):
    def __init__(self, system_prompt: str, system_tokens: int, max_tokens: int = 1000):
        super().__init__(max_tokens=max_tokens)
        self.system_tokens = system_tokens
        self.add_message('system', system_prompt, system_tokens)
    def clear_history(self) -> None:
        self.messages = [self.messages[0]]
        self.current_tokens = self.system_tokens


sys_ctx = SystemContextManager(
    system_prompt="You are a helpful AI assistant.",
    system_tokens=20,
    max_tokens=100,
)
print("Сразу после создания:", sys_ctx.get_remaining_tokens())  # 80

sys_ctx.add_message("user", "Hello!", 30)
print("После сообщения:", sys_ctx.get_remaining_tokens(), len(sys_ctx.messages))  # 50 2

sys_ctx.clear_history()
print("После очистки:", sys_ctx.get_remaining_tokens(), len(sys_ctx.messages))  # 80 1

