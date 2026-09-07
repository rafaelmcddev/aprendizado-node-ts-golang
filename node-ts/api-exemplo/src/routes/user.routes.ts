import { Router } from 'express';
import * as userController from '../controllers/user.controller.js';

// Aqui a URL vira uma chamada de função. É o "urls.py"/"routes/web.php".
const router = Router();

router.get('/', userController.index);      // GET  /users
router.get('/:id', userController.show);    // GET  /users/1
router.post('/', userController.store);     // POST /users

export default router;
