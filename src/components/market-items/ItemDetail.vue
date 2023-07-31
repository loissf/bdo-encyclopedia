<template>
  <button type="button" @click="returnClick">Return</button>
  <div>TEST</div>
</template>

<script setup lang="ts">
import { useMarketStore, ViewType } from "@/components/market-store";
import { getItemOrders } from "@/queries";
import { ref } from "vue";
const marketStore = useMarketStore();

function returnClick() {
  marketStore.viewType = ViewType.ItemList;
}

const data = ref<unknown>();

if (marketStore.selectedItem) {
  getItemOrders(marketStore.selectedItem?.baseItem.id, 0).then(
    (result) => (data.value = data)
  );
}
</script>
