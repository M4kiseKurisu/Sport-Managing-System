import { createRouter, createWebHashHistory } from "vue-router";
import EBorrowMain from "./components/MainPage/Page/E-Borrow/EBorrowMain.vue"
import Borrow from "./components/MainPage/Page/E-Borrow/Borrow.vue"
import Personal from "./components/MainPage/Page/E-Borrow/Personal.vue"
import Group from "./components/MainPage/Page/E-Borrow/Group.vue"

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
                    path: 'Borrow/Personal',
                    component: Personal
                },
                {
                    path: 'Borrow/Group',
                    component: Group
                }
            ]
        }
    ]
});

export default router;