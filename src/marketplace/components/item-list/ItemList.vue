<template>
  <div v-if="category" class="item-list">
    <ul>
      <li v-for="item in category.items" :key="item.id">
        <ListItemComponent
          :item="item"
          @click="selectItem(item)"
        ></ListItemComponent>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { ListItem } from "@/models/Item";
import ListItemComponent from "./ListItemComponent.vue";
import { useMarketStore } from "@/marketplace/market-store";

const marketStore = useMarketStore();

const category = computed(() => marketStore.selectedCategory);

function selectItem(item: ListItem) {
  marketStore.selectItem(item.id);
}
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.item-list {
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;

  @include custom-scrollbar;
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
@/marketplace/market-store
