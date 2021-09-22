import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/Homepage'
    }, 
    {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: '/Homepage',
                name: 'HomePage',
                meta: {
                    title: '系统首页'
                },
                component: () => import(/* webpackChunkName: "history" */
                    '../views/Homepage.vue')
            },
            {
                path: "/dashboard",
                name: "dashboard",
                meta: {
                    title: '个人主页'
                },
                component: () => import(
                    /* webpackChunkName: "dashboard" */
                    "../views/Dashboard.vue")
            }, 
            {
                path: "/Search",
                name: "Search",
                meta: {
                    title: '搜索页面'
                },
                component: () => import(
                    /* webpackChunkName: "dashboard" */
                    "../views/Search.vue")
            },
            {
                path: '/404',
                name: '404',
                meta: {
                    title: '找不到页面'
                },
                component: () => import(/* webpackChunkName: "404" */
                    '../views/404.vue')
            },
            {
                path: '/sourceCode',
                name: 'sourceCode',
                meta: {
                    title: '源代码上传页面'
                },
                component: () => import(/* webpackChunkName: "sourceCode" */
                    '../views/fuzzing/sourceCode.vue')
            },
            {
                path: '/history',
                name: 'history',
                meta: {
                    title: '历史记录'
                },
                component: () => import(/* webpackChunkName: "history" */
                    '../views/fuzzing/history.vue')
            },
            {
                path: '/wait',
                name: 'wait',
                meta: {
                    title: '等待页面'
                },
                component: () => import(/* webpackChunkName: "wait" */
                    '../views/fuzzing/wait.vue')
            },
            {
                path: '/sourceProgram',
                name: 'sourceProgram',
                meta: {
                    title: '可执行文件上传页面'
                },
                component: () => import(/* webpackChunkName: "sourceProgram" */
                    '../views/fuzzing/sourceProgram.vue')
            },
            {
                path: '/usetext',
                name: 'usetext',
                meta: {
                    title: '使用教程'
                },
                component: () => import(/* webpackChunkName: "sourceProgram" */
                    '../views/fuzzing/usetext.vue')
            },
            {
                path: "/tabs",
                name: "tabs",
                meta: {
                    title: 'tab标签'
                },
                component: () => import (
                /* webpackChunkName: "tabs" */
                "../views/Tabs.vue")
            }
        ]
    }, {
        path: "/login",
        name: "Login",
        meta: {
            title: '登录'
        },
        component: () => import(
            /* webpackChunkName: "login" */
            "../views/Login.vue")
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | vue-manage-system`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permission) {
        // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
        role === 'admin'
            ? next()
            : next('/403');
    } else {
        next();
    }
});

export default router;