<template>
    <el-table :data="filteredUsers" style="width:100%">

        <el-table-column label="呢称" width="150px">
            <template #default="scope">
                <div v-for="user in scope.row" :key="user.uid" class="user-info">
                    <div v-if="user.pic !== null">
                        <img :src="'http://127.0.0.1:8000' + user.pic" class="avatar" />
                    </div>
                    <div v-else>
                        <img :src="defaultImage" class="avatar" />
                    </div>
                    <span>{{ user.user_name }}</span>
                </div>
            </template>
        </el-table-column>

        <el-table-column label="类型" width="92px">
            <template #default="scope">
                <div v-for="user in scope.row" :key="user.uid">
                    <span>{{ user.type }}</span>
                </div>
            </template>
        </el-table-column>

        <el-table-column>
            <template #header>
                <div class="searchTitle">
                    <div class="searchBox">
                        <el-input v-model="keyword" placeholder="搜索成员"></el-input>
                    </div>
                    <el-button @click="search" class="searchButton">查询</el-button>
                </div>
            </template>
            <template #default="scope" align="right">
                <div v-for="user in scope.row" :key="user.uid" class="user-info">
                    <div v-if="this.father == 'YourGroup'" class="button-container">
                        <el-button v-if="this.group.type == '创建人' || this.group.type == '管理员'" size="small" type="danger"
                            @click="handleDelete(user.uid)">踢出</el-button>
                        <el-button v-if="this.group.type == '创建人'" size="small" type="warning" @click="handleSet(user)">
                            <span v-if="user.type == '管理员'">移除权限</span>
                            <span v-if="user.type == '成员'">设为管理员</span>
                        </el-button>
                    </div>
                </div>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
</script>