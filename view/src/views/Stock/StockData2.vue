<template>
  <div class="homeward">
    <el-container class="main_container">
      <el-aside width="20%" class="{['absolute top-0 left-0 h-full']}" visibility="false">
        <div style="width: 100%; height: 100%">
          <div style="width: 100%; height: 95%">
            <el-check-tag
              style="margin-right: 8px"
              v-for="tag in reativeObject.grouplist"
              :key="tag"
              class="mx-1"
              closable
              :checked="tag == activetag"
              :disable-transitions="false"
              @close="handleClose(tag)"
              @change="onChange(tag)"
            >
              {{ tag }}
            </el-check-tag>
            <el-input
              v-if="inputVisible"
              ref="InputRef"
              v-model="inputValue"
              class="ml-1 w-20"
              size="small"
              @keyup.enter="handleInputConfirm"
              @blur="handleInputConfirm"
            />
            <el-button v-else class="button-new-tag ml-1" size="small" @click="showInput">
              +
            </el-button>

            <el-table :data="reativeObject.stockist" style="width: 100%" height="96%" width="100%">
              <el-table-column label="Date" width="75" fixed sortable>
                <template #header>
                  <span>代码</span>
                </template>
                <template #default="scope">
                  <p>{{ scope.row.name }}</p>
                  <p>{{ scope.row.code }}</p>
                </template>
              </el-table-column>

              <el-table-column prop="name" label="Name" width="60" show-overflow-tooltip sortable>
                <template #header>
                  <span>涨</span>
                </template>
              </el-table-column>
              <el-table-column
                prop="address"
                label="Address"
                width="60"
                show-overflow-tooltip
                sortable
              >
                <template #header>
                  <span>地址</span>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div style="height: 5%">
            <el-pagination
              small
              layout="prev, pager, next"
              :total="50"
              style="height: 100%, background-color"
            />
          </div>
        </div>
      </el-aside>
      <el-main class="stock_main_1">
        <el-scrollbar>
          <StockData />
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import {
  ElContainer,
  ElMain,
  ElScrollbar,
  ElAside,
  ElTable,
  ElTableColumn,
  ElPagination,
  ElCheckTag,
  ElInput,
  ElButton
} from 'element-plus'
import StockData from './StockData.vue'
import { onMounted, reactive, ref, nextTick } from 'vue'

import { getMyGroupApi, addGroupApi, groupStockListApi } from '@/api/stock'
const reativeObject = reactive({
  stockist: [],
  grouplist: []
})
const activetag = ref('')
const onChange = (val) => {
  activetag.value = val
}
const inputVisible = ref(false)
const inputValue = ref('')
const handleClose = (tag: string) => {
  reativeObject.grouplist.splice(reativeObject.grouplist.indexOf(tag), 1)
}

const InputRef = ref<InstanceType<typeof ElInput>>()
const handleInputConfirm = () => {
  if (inputValue.value) {
    reativeObject.grouplist.push(inputValue.value)
    addGroupApi({ name: inputValue.value })
  }
  inputVisible.value = false
  inputValue.value = ''
}
const showInput = () => {
  inputVisible.value = true
  nextTick(() => {
    InputRef.value!.input!.focus()
  })
}
onMounted(async () => {
  let grouplist = await getMyGroupApi()
  grouplist.data.forEach((element) => {
    reativeObject.grouplist.push(element.name)
  })
  if (reativeObject.grouplist.length > 0) {
    activetag.value = reativeObject.grouplist[0]
  }
  let stocklist = await groupStockListApi({ groupName: activetag.value })
  stocklist.data.forEach((element) => {
    reativeObject.stockist.push({ name: element.name, code: element.code })
  })
  console.log(reativeObject.stockist)
})
</script>

<style scoped>
.homeward {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.main_container {
  height: 100%;
}
.main_container {
  height: 100%;
}
.el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.stock_main_1 {
  padding: 0;
}
</style>
