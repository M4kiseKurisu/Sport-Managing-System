<template>
  <div class="common-layout">
    <el-container>

      <el-aside width="200px" class="centered-aside">
        <div class="group-info">
          <!-- Left section for group information -->
          <div class="group-details">
            <div class="center-content">
              <div v-if="group.image !== null">
                  <img :src="'http://127.0.0.1:8000' + group.image" class="image" />
              </div>
              <div v-else>
                  <img :src="defaultImage" class="image" />
              </div>
              <div class="group_name">
                <h1>{{ group.name }}</h1>
              </div>
              <div class="group-buttons"  v-if="this.father=='YourGroup' 
              && (this.group.type=='创建者' || this.group.type=='管理者')">
                <el-button @click="addActivity()">新增活动</el-button>
              </div>
            </div>
          </div>
        </div>
      </el-aside>


      <el-main width="20%">
        <div class="group-navigation">
          <!-- Right section for navigation -->
          <el-card>
            <el-collapse v-model="activeName" accordion>
              <el-collapse-item name="1" class="group_instrudiction">
                <template #title class = "collapse_title">
                  <span class="custom-collapse-title">团体简介</span>
                </template>
                <p>{{ group.description }}</p>
              </el-collapse-item>
            </el-collapse>
          </el-card>
          <ul>
            <el-card><li>团体活动</li></el-card>
            <el-card @click="drawer = true">
              <li>团体成员</li>
            </el-card>
            <!-- Add more navigation links as needed -->
          </ul>
        </div>
      </el-main>
    </el-container>

      <el-drawer v-model="drawer" title="成员列表" :with-header="false" width="400px">
        <el-table :data="filteredTableData" style="width:400px">

          <el-table-column label="呢称" width="150px">
            <template #default="scope">
              <div class="user-info">
                <img :src="getAvatar(scope.row)" alt="avatar" class="avatar">
                <span>{{ scope.row.name }}</span>
              </div>
            </template>
          </el-table-column>
          
          <el-table-column label="类型">
            <template #default="scope">
              <span>{{scope.row.type }}</span>
            </template>
          </el-table-column>  

          <el-table-column  width="150px">
            <template #header>
              <el-input v-model="search" size="small" placeholder="Type to search" />
            </template>
            <template #default="scope" align="right">
              <div v-if="this.father=='YourGroup'" class="button-container">
              <el-button
                v-if="this.group.type=='创建者' || this.group.type=='管理者'"
                size="small"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button>
              <el-button
                v-if="this.group.type=='创建者'"
                size="small"
                type="warning"
                @click="handleDelete(scope.$index, scope.row)"
              >设为管理员</el-button>
            </div>
            </template>
          </el-table-column>

        </el-table>

        <el-pagination
        :small="small"
        :disabled="disabled"
        :background="background"
        layout="prev, pager, next"
        :page-size="10"
        :total="totalPages"
        v-model:current-page="currentPage"
        @current-change="handleCurrentChange"
        />
      </el-drawer>

  </div>
</template>

<script lang="ts">
import { computed, ref } from 'vue'

export default {
  data() {  
    return {
      drawer: false,
      group: {
        image: './src/images/group-default-picture.png', // Replace with your group image path
        name: '团体名称',
        description: '团体简介描述',
        type: ''
      },
      father: ''
    };
  },

  mounted() {
    // 获取传递的参数
    const groupName = this.$route.query.groupName;
    const description = this.$route.query.description;
    const image = this.$route.query.image;
    const father = this.$route.query.father;
    const type = this.$route.query.type;

    // 将参数存储在 group 对象中
    this.group.name = groupName;
    this.group.description = description;
    this.group.image = image;
    this.group.type = type;
    this.father = father;
  },

  methods: {
    addActivity() {
      // 处理新增活动的逻辑
    },
  },

  setup() {
    const defaultImage = "./src/images/group-default-picture.png"
    const activeName = ref('1');

    interface User {
      name: string;
      avatar: string;
      description: string;
      type: string
    }

    const small = ref(false);
    const background = ref(false);
    const disabled = ref(false);

    const search = ref('');
    const currentPage = ref(1);
    const totalPages = computed(() => {
      console.log(Math.ceil(filterTableData.value.length));
      return Math.ceil(filterTableData.value.length);
    });
    const filterTableData = computed(() =>
      tableData.filter(
        (data) =>
          !search.value ||
          data.name.includes(search.value)
      )
    );
    const filteredTableData = computed(() => {
      const start = (currentPage.value - 1) * 10;
      const end = start + 10;
      return filterTableData.value.slice(start, end);
    });

    const handleCurrentChange = (val: number) => {
      console.log(`current page: ${val}`);
    };

    const handleDelete = (index: number, row: User) => {
      console.log(index, row);
    };

    const tableData: User[] = [
      {
        name: 'Tom',
        avatar: './src/images/emptyAvatar.png',
        description: '这个人很懒，还没有编写签名',
        type: '创建人'
      },
      // ...其他用户数据...
    ];

    const getAvatar = (user: User) => user.avatar;

    // 返回需要在组件中使用的值和函数
    return {
      small,
      background,
      disabled,
      search,
      currentPage,
      totalPages,
      filterTableData,
      filteredTableData,
      handleCurrentChange,
      handleDelete,
      tableData,
      getAvatar,
      activeName,
      defaultImage
    };
  }
};

</script>

<style scoped>
/* Adjustments for group information section */
.common-layout {
  display: flex;
  max-width: 80%;
  max-height: 100%;
  margin: 20px;
  background-color: #f1e9fd;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.group-info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.group-details {
  text-align: right;
}
.group_name{
  font-size: 23px;
  text-align: center;
}
.group-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px; /* Added border-radius */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

/* Adjustments for navigation section */
.group-navigation {
  display: flex;
  flex-direction: column;
  margin-left: 100px;
  text-align: left;
}

.group-navigation h2 {
  font-size: 20px;
  margin-bottom: 10px;
  color: #333;
}

.group-navigation ul {
  list-style: none;
  padding: 0;
}

.group-navigation li {
  font-size: 16px;
  font-weight: bold;
  color: #666;
  margin-bottom: 10px;
}

.group-navigation a {
  text-decoration: none;
  color: #666;
  font-weight: bold;
  transition: color 0.3s ease;
}

.group-navigation a:hover {
  color: #333;
}

.group_instrudiction p{
  font-family: Arial, sans-serif; /* 修改字体 */
  font-size: 14px; /* 修改字体大小 */
  line-height: 1.5; /* 修改行高 */
  color: #555;
}

.custom-collapse-title {
  font-size: 16px;
  font-weight: bold;
  color: #666;
  border-radius: 10px;
  display: inline-block; /* 让标题内容成为一个块级元素 */
  cursor: pointer; /* 添加鼠标指针样式 */
}

.centered-aside {
  display: flex;
  justify-content: center;
  align-items: center;
}

.center-content {
  text-align: center;
}

.user-info {
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.group-buttons {
  margin-top: 20px;
}

.button-container {
  display: flex;
  justify-content: space-between; /* 可以根据需要选择其他布局方式 */
}

.image {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
