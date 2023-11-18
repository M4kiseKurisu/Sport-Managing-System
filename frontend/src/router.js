import { createRouter, createWebHashHistory } from "vue-router";
import EBorrowMain from "./components/MainPage/Page/E-Borrow/EBorrowMain.vue"
import Borrow from "./components/MainPage/Page/E-Borrow/Borrow.vue"
import Personal from "./components/MainPage/Page/E-Borrow/Personal.vue"

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
        }
    ]
});

export default router;