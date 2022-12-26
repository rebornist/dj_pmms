
document.getElementById("workspaceCreate").onclick = getWorkspaceForm;


function getWorkspaceForm() {
    /* 통신에 사용 될 XMLHttpRequest 객체 정의 */
    httpRequest = new XMLHttpRequest();
    /* httpRequest의 readyState가 변화했을때 함수 실행 */
    httpRequest.onreadystatechange = () => {
        /* readyState가 Done이고 응답 값이 200일 때, 받아온 response로 name과 age를 그려줌 */
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                const result = httpRequest.response;
                console.log(result);
            } else {
                alert('Request Error!');
            }
        }
    };

    /* Get 방식으로 name 파라미터와 함께 요청 */
    httpRequest.open('GET', '/workspaces/create');
    
    /* 정의된 서버에 요청을 전송 */
    httpRequest.send();
}