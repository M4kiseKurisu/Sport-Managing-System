<template>
<div class="button-row">
  <!-- 创建团体按钮和创建逻辑 -->
  <el-button text @click="showCreateGroup = true">创建团体</el-button>

  <el-dialog title="创建团体" v-model="showCreateGroup" width="60%">
    <el-form :model="form" label-width="120px" :rules="rules">
      <el-form-item label="团体名称" prop="name">
        <el-input v-model="form.name" style="width: 150px;"  maxlength="10" show-word-limit />
      </el-form-item>
      <el-form-item label="人数上限" prop="max">
        <el-input v-model="form.max" style="width: 150px;"/>
      </el-form-item>
      <el-form-item label="Tag" prop="Tag">
        <el-select v-model="form.tag" placeholder="请选择你的Tag">
          <el-option label="娱乐" value="娱乐" />
          <el-option label="竞技" value="竞技" />
          <el-option label="综合" value="综合" />
        </el-select>
      </el-form-item>


      <!-- 上传逻辑 -->
      <el-form-item label="上传头像" prop="pic">
        <el-upload action="#" 
          list-type="picture-card" 
          :auto-upload="false" 
          :limit="1" 
          :on-remove="handleRemove"
          v-model:file-list="this.form.pic"
        >
          <el-icon><Plus /></el-icon>

          <template #file="{ file }">
            <div>
              <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
              <span class="el-upload-list__item-actions">
                <span
                  class="el-upload-list__item-preview"
                  @click="handlePicturePre(file)">
                  <el-icon><zoom-in /></el-icon>
                </span>
                <span
                  class="el-upload-list__item-preview"
                  @click="handleRemove(file,this.form.pic)">
                  <el-icon><Delete /></el-icon>
                </span>
              </span>
            </div>
          </template>

          <template #tip>
            <div class="el-upload__tip"  style="color: red;">
              最多上传一张图片
            </div>
          </template>
        </el-upload>

        <el-dialog v-model="dialogVisible">
          <img w-full :src="dialogImageUrl" alt="Preview Image" />
        </el-dialog>



        <!-- 上传逻辑 -->
      </el-form-item>

      <el-form-item label="团体简介">
        <el-input v-model="form.desc" type="textarea"  maxlength="50" show-word-limit/>
      </el-form-item>

    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="showCreateGroup = false">取消</el-button>
        <el-button type="primary" @click="onSubmit">
           提交
        </el-button>
      </span>
    </template>
  </el-dialog>
  <div class="searchTitle">
    <div class="searchBox">
      <el-input v-model="keyword" placeholder="输入查询信息"></el-input>
    </div>
    <el-button @click="search">查 询</el-button>
  </div>
</div>
<!-- 创建团体按钮和创建逻辑 -->


<!-- 分页逻辑 -->
<div>
    <el-scrollbar class="scrollbar" max-height="100%">
      <el-row v-for="(page, index) in paginatedGroups" :key="index">
        <el-col v-for="card in page" :key="card.gid"  :span="8">
          <div>
            <group-card :card="card" :status="getCardStatus()" :msg="this.msg"/>
          </div>
        </el-col> 
      </el-row>
    </el-scrollbar>
    <el-pagination
      :current-page="currentPage"
      :page-size=9
      :total="this.groupList.length"
      @current-change="handlePageChange"
    ></el-pagination>
  </div>
</template>
<!-- 分页逻辑 -->



<script lang="ts">
import {reactive, ref} from 'vue'
import GroupCard from "../../Components/GroupCard.vue";
import axios from 'axios'
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import { type UploadFile, type UploadProps, ElMessage} from 'element-plus' 

export default {
  data() {
    return {
      groupList: [], // 从后端获取的所有团体数据 
      currentPage: 1, // 当前页码
      input: "",
      keyword: "",
      status: "",
      msg: "",
    }
  },
  components: {
    GroupCard,
    Delete, 
    Download, 
    Plus, 
    ZoomIn,
  },
  created() {
    const storedUid = sessionStorage.getItem('uid');
      if (storedUid) {
        const uid = JSON.parse(storedUid);
        axios({
          method: "GET",
          url: "http://127.0.0.1:8000/api/group/view",
          params: {
            uid: uid
          }
        }).then((result) => {
          this.groupList = result.data.list;
          this.status = result.data.status;
          this.msg = result.data.msg;
        }).catch((error) => {
          console.error('Error fetching group data:', error);
        });
    } else {
        console.error('UID not found in sessionStorage');
    }
  },
  computed: {
    paginatedGroups() {
      if (this.groupList.length === 0) {
          return []; // 如果 groupList 是空数组，直接返回空数组
      }

      const pages: any[]= [];
      console.log(this.groupList)
      for(let i = 0; i < this.groupList.length; i += 9){
        pages.push(this.groupList.slice(i, i+9));
      }

      const currentPage = this.currentPage;
      const page = pages[currentPage - 1];
      const groups: any[] = [];

      for(let i = 0; i < page.length; i+=3){
        groups.push(page.slice(i,i+3));
      }

      return groups;
    },
    
  },
  methods: {
    getCardStatus() {
      // 示例：根据团队信息判断状态
       return this.status;
    },
    handlePageChange(newPage) {
      // 当页码变化时更新当前页码
      this.currentPage = newPage;
    },
    search() {
          axios({
              method: "GET",
              url: "http://127.0.0.1:8000/api/group/view",
              params: {
                  uid: sessionStorage.getItem('uid'),
                  keyword: this.keyword
              }
          }).then((result) => {
              this.groupList = result.data.list   
          });
    },
    onSubmit () {
      if(this.form.name && this.form.max 
        && this.form.tag && this.form.pic.length !=0){
          let desc = this.form.desc
          if(!desc){
              desc="这个负责人很懒，还没填写简介~"
          }
          const pic = this.form.pic[0].raw
          const data = new FormData();
          const uid = sessionStorage.getItem('uid');
          if (uid) {
              data.append('uid', uid);
          }
          data.append('group_name', this.form.name);
          data.append('group_desc', desc);
          data.append('maximum', this.form.max);
          data.append('tag', this.form.tag);
          data.append('picture', pic);
          axios.post('http://127.0.0.1:8000/api/group/create', data)
              .then(response => {
              // 处理响应
              console.log(response);
          }).catch(error => {
              console.error(error);
          });

          this.showCreateGroup = false
      }else{
          ElMessage.error('请填写必填项！');
      }
    }
  },
  setup() {
    const showCreateGroup = ref(false)
    const dialogImageUrl = ref('')
    const dialogVisible = ref(false)
    const disabled = ref(false)

    const rules = {
      name: [
        { required: true, message: '请填写团体名称', trigger: 'blur' },
      ],
      max: [
        { required: true, message: '请填写人数上限', trigger: 'blur' },
      ],
      Tag: [
        { required: true, message: '请选择标签', trigger: 'blur' },
      ],
      pic: [
        { required: true, message: '请上传图片', trigger: 'blur' },
      ],
    };


    const form = reactive({
      name: '',
      max: '',
      desc: '',
      tag: '',
      pic: []
    })
    
    const handlePicturePre = (file: UploadFile) => {
      dialogImageUrl.value = file.url!
      dialogVisible.value = true
    }

    const handleRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
      //console.log("delete")
        // uploadFile 是要移除的文件对象
        const index = uploadFiles.indexOf(uploadFile);
        if (index !== -1) {
            uploadFiles.splice(index, 1); // 从上传文件列表中移除文件
            uploadFile.url = '';
        }
        dialogImageUrl.value = '';
    }

    return{
      showCreateGroup,
      form,
      Delete, 
      Download, 
      Plus, 
      ZoomIn,
      handlePicturePre,
      disabled,
      dialogVisible,
      dialogImageUrl,
      handleRemove,
      rules
    }
  }
}
</script>
  
<style scoped>
.searchTitle {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.searchBox {
    width: 240px;
}

.button-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>