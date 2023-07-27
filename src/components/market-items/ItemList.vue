<template>
  <div v-if="selectedItem" class="item-detail">
    <button type="button" @click="selectedItem = undefined">Return</button>
    <template v-if="selectedItem.subList.length > 0">
      <ListItemComponent
        class="base-item"
        :item="selectedItem.baseItem"
      ></ListItemComponent>
      <ul>
        <li v-for="item in selectedItem.subList" :key="item.id">
          <ListItemComponent :item="item"></ListItemComponent>
        </li>
      </ul>
    </template>
    <template v-else>
      <ItemDetail></ItemDetail>
    </template>
  </div>
  <div v-else class="item-list">
    <ul>
      <li v-for="item in items" :key="item.id">
        <ListItemComponent
          :item="item"
          @click="selectItem(item)"
        ></ListItemComponent>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { ListItem, SubList } from "@/models/Item";
import ListItemComponent from "./ListItemComponent.vue";
import ItemDetail from "./ItemDetail.vue";
import { getItem } from "@/queries";

const props = defineProps({
  items: {
    type: Object as () => Array<ListItem>,
    required: true,
  },
});

const selectedItem = ref<SubList>();

async function selectItem(item: ListItem) {
  selectedItem.value = (await getItem(item.id)) ?? {
    baseItem: item,
    subList: [],
  };
}
</script>

<style scoped lang="scss">
.item-list {
}

.item-detail {
  .base-item {
    margin-bottom: 1.5rem;
  }
}

ul {
  width: 100%;

  padding: 0;
  margin: 0;

  overflow-y: auto;

  li {
    display: block;
    width: 100%;

    &:not(:last-child) {
      margin-bottom: 0.375rem;
    }
  }
}
</style>
