<template>
    <div>
        <el-breadcrumb :separator-icon="ArrowRight" class="custom-breadcrumb">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item v-for="(item, index) in breadcrumbItems" :key="index">
                <router-link :to="item.to" class="custom-link"
                    :class="{ 'last-item': index === breadcrumbItems.length - 1 }">{{ item.label }}</router-link>
            </el-breadcrumb-item>
        </el-breadcrumb>

        <!-- 其他页面内容 -->
        <!-- ... -->
    </div>
</template>

<script>
import { ArrowRight } from '@element-plus/icons-vue'
export default {
    data() {
        return {
            breadcrumbItems: [], // 存储面包屑路径信息
            ArrowRight
        };
    },
    components: {
        ArrowRight
    },
    watch: {
        // 监听路由变化，在路由变化时更新面包屑信息
        $route(to, from) {
            this.updateBreadcrumb(to.matched);
        }
    },
    created() {
        // 初始化页面时构建面包屑
        this.updateBreadcrumb(this.$route.matched);
    },
    methods: {
        updateBreadcrumb(matched) {
            const breadcrumbs = [];
            matched.forEach(route => {
                if (route.meta && route.meta.breadcrumbLabel) {
                    breadcrumbs.push({
                        label: route.meta.breadcrumbLabel,
                        to: route.path
                    });
                }
            });
            this.breadcrumbItems = breadcrumbs;
        }
    }
};
</script>

<style scoped>
/* 自定义面包屑样式 */
.custom-breadcrumb {
    font-size: 18px;
    /* 调整字体大小 */
}

/* 自定义链接样式 */
.custom-link {
    color: #f1efef !important;
    /* 设置浅色系颜色 */
}

/* 最后一个面包屑项样式 */
.last-item {
    color: rgb(218, 217, 217) !important;
    /* 设置最后一个面包屑项的颜色 */
}
</style>
