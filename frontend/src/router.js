import { createRouter, createWebHashHistory } from "vue-router"
import store from './store'

import Login from "./components/Login/Login.vue"
import MainPage from "./components/MainPage/MainPageContainer.vue"

import UserInformation from "./components/MainPage/Page/UserInformation.vue"

import EBorrowMain from "./components/MainPage/Page/E-Borrow/EBorrowMain.vue"
import Borrow from "./components/MainPage/Page/E-Borrow/Borrow.vue"
import Personal from "./components/MainPage/Page/E-Borrow/Personal.vue"
import Group from "./components/MainPage/Page/E-Borrow/Group.vue"

import GroupInformation from "./components/MainPage/Page/GroupInformation.vue"
import YourGroup from './components/MainPage/Page/Group/YourGroup.vue'
import GroupList from './components/MainPage/Page/Group/GroupList.vue'
import YourApplication from './components/MainPage/Page/Group/YourApplication.vue'
import PendingReview from './components/MainPage/Page/Group/PendingReview.vue'
import Details from './components/MainPage/Page/Group/Details.vue'

import Friend from './components/MainPage/Page/FriendInformation.vue'

import Activity from './components/MainPage/Page/Activity/ActivityMain.vue'
import ActivityInformation from './components/MainPage/Page/Activity/ActivityInformation.vue'
import ActivityBefore from './components/MainPage/Page/Activity/ActivityBefore.vue'
import ActivityDetail from './components/MainPage/Page/Activity/ActivityDetail.vue'

import MyActivityMain from './components/MainPage/Page/MyActivity/MyActivityMain.vue'
import MyActivityShow from './components/MainPage/Page/MyActivity/MyActivityShow.vue'
import MyActivityApply from './components/MainPage/Page/MyActivity/MyActivityApply.vue'
import MyActivityApplyMain from './components/MainPage/Page/MyActivity/MyActivityApplyMain.vue'
import MyActivitySelectField from './components/MainPage/Page/MyActivity/MyActivitySelectField.vue'
import MyActivityResultShow from './components/MainPage/Page/MyActivity/MyActivityResultShow.vue'


const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '',
            redirect: '/Login'
        },
        {
            path: '/Login',
            component: Login,
            meta: {
                requireAuth: false
            }
        },
        {
            path: '/Page',
            component: MainPage,
            redirect: '/Page/User_Information',
            meta: {
                requireAuth: true
            },
            children: [
                {
                    path: 'Borrow_Equipment',
                    component: EBorrowMain,
                    redirect: '/Page/Borrow_Equipment/Equipment_Information',
                    children: [
                        {
                            path: 'Equipment_Information',
                            component: Borrow
                        },
                        {
                            path: 'Borrow/Personal',
                            component: Personal
                        },
                        {
                            path: 'Borrow/Group',
                            component: Group
                        }
                    ]
                },
                {
                    path: 'User_Information',
                    component: UserInformation
                },
                {
                    path: 'Activity_Information',
                    component: Activity,
                    redirect: '/Page/Activity_Information/Show',
                    children: [
                        {
                            path: 'Show',
                            component: ActivityInformation
                        },
                        {
                            path: 'Before',
                            component: ActivityBefore
                        },
                        {
                            path: 'Detail/:aid',
                            component: ActivityDetail
                        }
                    ]
                },
                {
                    path: 'MyActivity',
                    component: MyActivityMain,
                    redirect: '/Page/MyActivity/Show',
                    children: [
                        {
                            path: 'Show',
                            component: MyActivityShow
                        },
                        {
                            path: 'Apply',
                            component: MyActivityApplyMain,
                            redirect: '/Page/MyActivity/Apply/Basic',
                            children: [
                                {
                                    path: 'Basic',
                                    component: MyActivityApply
                                },
                                {
                                    path: 'Field',
                                    component: MyActivitySelectField
                                },
                                {
                                    path: 'Result',
                                    component: MyActivityResultShow
                                }
                            ]
                        }
                    ]
                },
                {
                    path: 'GroupInformation',
                    component: GroupInformation,
                    redirect: '/Page/GroupInformation/GroupList',
                    children: [
                        {
                            path: 'YourGroup',
                            component: YourGroup
                        },
                        {
                            path: 'GroupList',
                            component: GroupList
                        },
                        {
                            path: 'YourApplication',
                            component: YourApplication
                        },
                        {
                            path: 'PendingReview',
                            component: PendingReview
                        },
                        {
                            path: 'Details',
                            name: 'Details',
                            component: Details,
                        }
                    ]
                },
                {
                    path: 'Friend',
                    component: Friend
                }
            ]
        }
    ]

});

// 添加全局前置守卫
router.beforeEach((to, from, next) => {
    // 检查是否需要登录才能访问
    if (to.matched.some(record => record.meta.requireAuth)) {
        // 通过对 store.state.user 有无值的检查来判断用户是否登录
        if (JSON.parse(sessionStorage.getItem('uid')) == null
            || JSON.parse(sessionStorage.getItem('user_name')) == null) {
            next({
                path: '/Login',
                query: { redirect: to.fullPath }
                // 将希望导航到的路由的路径传给登录界面，登录成功后可能需要基于此进行重定向。
            })
        } else {
            next()  // 如果用户已经登录，就正常进入该路由。
        }
    } else {
        next()  // 如果不需要登录，则直接放行。
    }
})

export default router;