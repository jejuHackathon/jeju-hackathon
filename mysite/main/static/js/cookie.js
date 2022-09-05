export const getCookie = (nickname) => {
    let name = nickname + "=";
    let ca = document.cookie.split(';');
    
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

export const setCookie = (nickname) => {
    document.cookie = "nickname=" + nickname;
}

export const deleteCookie = () => {
    document.cookie = 'nickname=; expires=Thu, 01 Jan 1999 00:00:10 GMT;';
}