import { getCookie } from './cookie.js';

export default function Router() {
    const { pathname } = location;

    const checkRouterByCookie = () => {
        if(pathname !== '/') {
            const nickname = getCookie('nickname');
            if(!nickname) location.href = "/";
        }
    }

    checkRouterByCookie();
}

Router();