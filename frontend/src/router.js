import { createRouter, createWebHashHistory } from "vue-router";
import EBorrowMain from "./components/MainPage/Page/E-Borrow/EBorrowMain.vue"
import Borrow from "./components/MainPage/Page/E-Borrow/Borrow.vue"
import Personal from "./components/MainPage/Page/E-Borrow/Personal.vue"
import Group from "./components/MainPage/Page/GroupInformation.vue"
import YourGroup from './components/MainPage/Page/Group/YourGroup.vue'
import GroupList from './components/MainPage/Page/Group/GroupList.vue'
import YourApplication from './components/MainPage/Page/Group/YourApplication.vue'
import PendingReview from './components/MainPage/Page/Group/PendingReview.vue'
import GroupMainPage from './components/MainPage/Page/Group/GroupMainPage.vue';

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/Borrow_Equipment',
            component: EBorrowMain,
            children: [
                {
                    path: 'Equipment_Information',
                    component: Borrow
                },
                {
                    path: 'Personal_Borrow',
                    component: Personal
                }
            ]
        },
        {
            path: '/Group',
            component: Group,
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
              }
            ]
          },
          {
            path: '/GroupMainPage', // 新的路径
            component: GroupMainPage, // GroupMainPage 组件
          }
    ]
});

export default router;