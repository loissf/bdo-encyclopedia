<template>
  <button type="button" @click="returnClick">Return</button>
  <div v-if="itemSubList" class="item-detail">
    <ListItemComponent
      class="base-item"
      :item="itemSubList.baseItem"
    ></ListItemComponent>
    <ul>
      <li v-for="item in itemSubList.subList" :key="item.id">
        <ListItemComponent
          :item="item"
          @click="selectItem(item)"
        ></ListItemComponent>
      </li>
    </ul>
  </div>
  <div v-else>ERROR</div>
</template>

<script setup lang="ts">
import ListItemComponent from "./ListItemComponent.vue";
import { useMarketStore, ViewType } from "@/components/market-store";
import { SubListItem } from "@/models/Item";
import { computed } from "vue";

const marketStore = useMarketStore();

const itemSubList = computed(() => marketStore.selectedItem);

function selectItem(item: SubListItem) {
  marketStore.selectEnhancement(item);
}

function returnClick() {
  marketStore.viewType = ViewType.ItemList;
}
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";
.item-detail {
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;

  @include custom-scrollbar;

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
