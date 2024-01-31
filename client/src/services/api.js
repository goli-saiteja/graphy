import api from 'services/http';
import {
    GET_METRICS_URL,
    GET_DEPARTMETS_URL
} from 'constants';

export const getMetrics = () => {
    return new Promise(async (resolve, reject) => {
        const getUrl = () => {
            return `${GET_METRICS_URL}`;
        };
        try {
            const url = getUrl();
            const data = await api.get(url)
            setTimeout(() => {
                resolve(data);
            }, 200);
        } catch (err) {
            reject(err);
        }
    });
};

export const getDepartments = () => {
    return new Promise(async (resolve, reject) => {
        const getUrl = () => {
            return `${GET_DEPARTMETS_URL}`;
        };
        try {
            const url = getUrl();
            const data = await api.get(url)
            setTimeout(() => {
                resolve(data);
            }, 200);
        } catch (err) {
            reject(err);
        }
    });
};