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
export const usedSoft = () => http.get("api/upload/availList/")
export const resultGet = () => http.get("api/result/")
export const processGet = (params) => http.post("api/process/",params)
export const searchGet = (params) => http.post("api/search/",params)
export const download = (params) => http.post("api/download/",params)
export const AnalyzeGet = (params) => http.post("api/analyze/",params)