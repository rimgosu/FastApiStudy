#!/bin/bash
git pull origin master
git add .

# ChatGPT API에 요청을 보내는 함수
summarize_changes() {
    local file_content=$1
    local api_key=$2

    # jq를 사용하여 JSON 데이터 생성 (messages 배열 추가)
    local data=$(jq -n \
                    --arg prompt "$file_content" \
                    --argjson max_tokens 100 \
                    '{model: "gpt-3.5-turbo", messages: [{"role": "system", "content": "Summarize for github commit message the following changes in English."}, {"role": "user", "content": $prompt}], max_tokens: $max_tokens}')

    # ChatGPT API를 사용하여 요청을 보내고 응답을 받음
    local response=$(curl -s -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $api_key" \
        -d "$data" \
        "https://api.openai.com/v1/chat/completions")

    # 응답에서 텍스트 내용을 추출
    echo $(echo $response | jq -r '.choices[0].message.content')
}


# Git에서 변경된 파일 목록을 가져옴
changed_files=$(git status -s | awk '{if ($1 == "M" || $1 == "A") print $2}')

# 변경된 파일들의 내용을 저장
content=""
for file in $changed_files; do
    # 비ASCII 문자를 제거
    content+="$(cat "$file" | tr -cd '\11\12\15\40-\176')"
done

# ChatGPT API 키를 환경 변수에서 가져옴
api_key=$GPT_API_KEY

# 변경 내용을 요약
commit_message=$(summarize_changes "$content" "$api_key")

# 커밋 메시지 확인
if [[ -z $commit_message ]]; then
    echo "커밋 메시지가 비어 있습니다."
    exit 1
fi

# 커밋
git commit -m "$commit_message"

# 푸시
git push origin master
