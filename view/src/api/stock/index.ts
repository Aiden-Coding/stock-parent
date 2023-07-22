import request from '@/config/axios'

export const getMyGroupApi = (): Promise<IResponse> => {
  return request.get({ url: '/group/grouplist' })
}

export const addGroupApi = (data: any): Promise<IResponse> => {
  return request.post({ url: '/group/add', data })
}

export const deleteGroupApi = (data: any): Promise<IResponse> => {
  return request.delete({ url: '/stock/myGroup/delete', data })
}
export const groupStockListApi = (data: any): Promise<IResponse> => {
  return request.post({ url: '/group/groupStock', data })
}

export const addStockApi = (groupId: any): Promise<IResponse> => {
  return request.post({ url: '/stock/myGroup/addStock', groupId })
}

export const deleteStockApi = (groupId: any, code: any): Promise<IResponse> => {
  return request.delete({ url: '/stock/myGroup/deleteStock', groupId, code })
}
