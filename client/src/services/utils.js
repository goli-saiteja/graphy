export const userInfo = () => {
    return JSON.parse(localStorage.getItem("user") || {});
}

export function debounce(cb, timer) {
    let clearTime;
    return (...args) => {
        clearTimeout(clearTime);
        clearTime = setTimeout(() => {
            cb.apply(this, args);
        }, timer)
    }
}