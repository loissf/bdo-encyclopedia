<template>
  <div v-if="item" class="detail" :grade="item.grade">
    <div class="header">
      <img class="icon" :src="item.icon" alt="" />
      <span class="name">{{ item.name }}</span>
      <button type="button" @click="returnClick">Return</button>
    </div>
    <div class="info">
      <div class="section">
        <label for="stock">In Stock</label>
        <span id="stock">{{ item.stock }}</span>
      </div>
      <div class="section">
        <label for="base-price">Base Price</label>
        <span id="base-price">{{ item.basePrice }}</span>
      </div>
      <div class="section">
        <label for="total-trades">Total Trades</label>
        <span id="total-trades">{{ item.totalTrades }}</span>
      </div>
      <div class="section">
        <label for="last-sale">Recent Transaction</label>
        <span id="last-sale">{{
          new Date(item.lastSale * 1000).toLocaleString()
        }}</span>
      </div>
    </div>
    <div class="graph"></div>
    <div class="orders">
      <ItemOrders />
    </div>
  </div>
</template>
<script setup lang="ts">
import { useMarketStore, ViewType } from "@/components/market-store";
import { computed } from "vue";
import ItemOrders from "./ItemOrders.vue";

const marketStore = useMarketStore();

const item = computed(() => marketStore.selectedEnhancement);

function returnClick() {
  marketStore.viewType = ViewType.ItemList;
}
</script>
<style scoped lang="scss">
.detail {
  display: grid;

  grid-template:
    "header orders" 1fr
    "info orders" 3fr
    "graph orders" 3fr /
    1fr auto;

  overflow: hidden;
  height: 100%;

  .header {
    grid-area: header;

    .icon {
      padding: 0.25rem;
      height: 2.5rem;
      width: 2.5rem;

      background-color: rgba(0, 0, 0, 0.65);
    }
  }

  .orders {
    grid-area: orders;
    overflow-y: auto;
  }

  .info {
    grid-area: info;

    display: grid;
    grid-template: auto auto / 1fr 1fr;

    justify-self: center;
    align-self: center;

    row-gap: 1.5rem;

    .section {
      display: flex;
      flex-direction: column;

      label {
        text-align: left;
        font-size: 80%;
        color: rgba(196, 196, 196, 0.75);
      }

      span {
        text-align: left;
        margin-top: 0.375rem;
      }
    }
  }

  .graph {
    grid-area: graph;
  }

  &[grade="0"] {
    .name {
      color: white;
    }
    .icon {
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(255, 255, 255, 0.4);
    }
  }

  &[grade="1"] {
    .name {
      color: rgba(0, 128, 0);
    }
    .icon {
      border: 1px solid rgba(0, 128, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(0, 128, 0, 0.4);
    }
  }

  &[grade="2"] {
    .name {
      color: rgba(60, 110, 255);
    }
    .icon {
      border: 1px solid rgba(60, 110, 255, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(60, 110, 255, 0.4);
    }
  }

  &[grade="3"] {
    .name {
      color: rgba(200, 200, 0);
    }
    .icon {
      border: 1px solid rgba(200, 200, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(200, 200, 0, 0.4);
    }
  }

  &[grade="4"] {
    .name {
      color: rgba(170, 0, 0);
    }
    .icon {
      border: 1px solid rgba(170, 0, 0, 0.6);
      box-shadow: 0px 0px 8px 0px rgba(170, 0, 0, 0.4);
    }
  }

  *::-webkit-scrollbar {
    width: 6px;
  }

  *::-webkit-scrollbar-track {
    background: #2b2b2b;
  }

  *::-webkit-scrollbar-thumb {
    background-color: #dfb14f;
    border-radius: 10px;
  }
}
</style>
