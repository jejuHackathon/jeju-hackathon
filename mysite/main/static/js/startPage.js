import { setCookie } from "./cookie.js";

export default function StartPage() {
    const nickNameInput = document.querySelector('.oreum-start__nickname');
    const learnButton = document.querySelector('.oreum-start__learn-button');
    let nickname = '';

    const init = () => {
        nickNameInput?.addEventListener('change', handleOnChangeNickName);
        learnButton?.addEventListener('click', handleOnClickLearnButton);
    }

    const handleOnChangeNickName = (e) => {
        nickname = e.target.value;
    }

    const handleOnClickLearnButton = () => {
        if(!nickname) {
            alert('값을 입력해주세요!')
            return;
        }
        setCookie(nickname);
        location.href = "/home";
    }

    init();
}

StartPage();