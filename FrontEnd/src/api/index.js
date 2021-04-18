import request from '../utils/request';
import http from "@/utils/http";

export const fetchData = query => {
    return request({
        url: './table.json',
        method: 'get',
        params: query
    });
};

// export const loginByPwd = (params) => http.post('/users/login/', params);
// export const formdataTest = (params) => http.post("upload/formdataTest/")
export const formdataTest = (params) => http.post("api/upload/sourceCode/",params)