# 닉네임 변경
# 1. 들어오는 메시지
# 2. 나가는 메시지
# 3. 변경 닉네임
# 3-1 채팅방 나가고 새로운 닉네임
# 3-2 채팅방에서 닉네임 변경
# 3-3 닉네임 변경시 출력된 메시지 닉네임도 변경됨

from collections import defaultdict

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	

answer = []

id_dict = defaultdict(str)

for record in records:
    temp_record = record.strip('"').split()
    
    if len(temp_record) > 2:
        command, chat_id, chat_nickname = temp_record
    else:
        command, chat_id = temp_record


    if command == 'Enter':
        answer.append((chat_id, command))
        id_dict[chat_id] = chat_nickname
        
    elif command == 'Leave':
        answer.append((chat_id, command))
        
    else:
        id_dict[chat_id] = chat_nickname

for i in range(len(answer)):
    message = ''
    if answer[i][1] == 'Enter':
        message = '님이 들어왔습니다."'
    else:
        message = '님이 나갔습니다."'
    answer[i] = '"' + id_dict[answer[i][0]] + message

print(answer)
